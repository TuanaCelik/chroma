# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromadb/proto/coordinator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromadb.proto import chroma_pb2 as chromadb_dot_proto_dot_chroma__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n chromadb/proto/coordinator.proto\x12\x06\x63hroma\x1a\x1b\x63hromadb/proto/chroma.proto\x1a\x1bgoogle/protobuf/empty.proto\"8\n\x14\x43reateSegmentRequest\x12 \n\x07segment\x18\x01 \x01(\x0b\x32\x0f.chroma.Segment\"\"\n\x14\x44\x65leteSegmentRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\xc2\x01\n\x12GetSegmentsRequest\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x11\n\x04type\x18\x02 \x01(\tH\x01\x88\x01\x01\x12(\n\x05scope\x18\x03 \x01(\x0e\x32\x14.chroma.SegmentScopeH\x02\x88\x01\x01\x12\x12\n\x05topic\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x17\n\ncollection\x18\x05 \x01(\tH\x04\x88\x01\x01\x42\x05\n\x03_idB\x07\n\x05_typeB\x08\n\x06_scopeB\x08\n\x06_topicB\r\n\x0b_collection\"X\n\x13GetSegmentsResponse\x12!\n\x08segments\x18\x01 \x03(\x0b\x32\x0f.chroma.Segment\x12\x1e\n\x06status\x18\x02 \x01(\x0b\x32\x0e.chroma.Status\"\xfa\x01\n\x14UpdateSegmentRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x05topic\x18\x02 \x01(\tH\x00\x12\x15\n\x0breset_topic\x18\x03 \x01(\x08H\x00\x12\x14\n\ncollection\x18\x04 \x01(\tH\x01\x12\x1a\n\x10reset_collection\x18\x05 \x01(\x08H\x01\x12*\n\x08metadata\x18\x06 \x01(\x0b\x32\x16.chroma.UpdateMetadataH\x02\x12\x18\n\x0ereset_metadata\x18\x07 \x01(\x08H\x02\x42\x0e\n\x0ctopic_updateB\x13\n\x11\x63ollection_updateB\x11\n\x0fmetadata_update\"\xc3\x01\n\x17\x43reateCollectionRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12-\n\x08metadata\x18\x03 \x01(\x0b\x32\x16.chroma.UpdateMetadataH\x00\x88\x01\x01\x12\x16\n\tdimension\x18\x04 \x01(\x05H\x01\x88\x01\x01\x12\x1a\n\rget_or_create\x18\x05 \x01(\x08H\x02\x88\x01\x01\x42\x0b\n\t_metadataB\x0c\n\n_dimensionB\x10\n\x0e_get_or_create\"s\n\x18\x43reateCollectionResponse\x12&\n\ncollection\x18\x01 \x01(\x0b\x32\x12.chroma.Collection\x12\x0f\n\x07\x63reated\x18\x02 \x01(\x08\x12\x1e\n\x06status\x18\x03 \x01(\x0b\x32\x0e.chroma.Status\"%\n\x17\x44\x65leteCollectionRequest\x12\n\n\x02id\x18\x01 \x01(\t\"i\n\x15GetCollectionsRequest\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x11\n\x04name\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x12\n\x05topic\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\x05\n\x03_idB\x07\n\x05_nameB\x08\n\x06_topic\"a\n\x16GetCollectionsResponse\x12\'\n\x0b\x63ollections\x18\x01 \x03(\x0b\x32\x12.chroma.Collection\x12\x1e\n\x06status\x18\x02 \x01(\x0b\x32\x0e.chroma.Status\"\xde\x01\n\x17UpdateCollectionRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\x05topic\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x11\n\x04name\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x16\n\tdimension\x18\x04 \x01(\x05H\x03\x88\x01\x01\x12*\n\x08metadata\x18\x05 \x01(\x0b\x32\x16.chroma.UpdateMetadataH\x00\x12\x18\n\x0ereset_metadata\x18\x06 \x01(\x08H\x00\x42\x11\n\x0fmetadata_updateB\x08\n\x06_topicB\x07\n\x05_nameB\x0c\n\n_dimension2\xb6\x05\n\x05SysDB\x12G\n\rCreateSegment\x12\x1c.chroma.CreateSegmentRequest\x1a\x16.chroma.ChromaResponse\"\x00\x12G\n\rDeleteSegment\x12\x1c.chroma.DeleteSegmentRequest\x1a\x16.chroma.ChromaResponse\"\x00\x12H\n\x0bGetSegments\x12\x1a.chroma.GetSegmentsRequest\x1a\x1b.chroma.GetSegmentsResponse\"\x00\x12G\n\rUpdateSegment\x12\x1c.chroma.UpdateSegmentRequest\x1a\x16.chroma.ChromaResponse\"\x00\x12W\n\x10\x43reateCollection\x12\x1f.chroma.CreateCollectionRequest\x1a .chroma.CreateCollectionResponse\"\x00\x12M\n\x10\x44\x65leteCollection\x12\x1f.chroma.DeleteCollectionRequest\x1a\x16.chroma.ChromaResponse\"\x00\x12Q\n\x0eGetCollections\x12\x1d.chroma.GetCollectionsRequest\x1a\x1e.chroma.GetCollectionsResponse\"\x00\x12M\n\x10UpdateCollection\x12\x1f.chroma.UpdateCollectionRequest\x1a\x16.chroma.ChromaResponse\"\x00\x12>\n\nResetState\x12\x16.google.protobuf.Empty\x1a\x16.chroma.ChromaResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chromadb.proto.coordinator_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CREATESEGMENTREQUEST']._serialized_start=102
  _globals['_CREATESEGMENTREQUEST']._serialized_end=158
  _globals['_DELETESEGMENTREQUEST']._serialized_start=160
  _globals['_DELETESEGMENTREQUEST']._serialized_end=194
  _globals['_GETSEGMENTSREQUEST']._serialized_start=197
  _globals['_GETSEGMENTSREQUEST']._serialized_end=391
  _globals['_GETSEGMENTSRESPONSE']._serialized_start=393
  _globals['_GETSEGMENTSRESPONSE']._serialized_end=481
  _globals['_UPDATESEGMENTREQUEST']._serialized_start=484
  _globals['_UPDATESEGMENTREQUEST']._serialized_end=734
  _globals['_CREATECOLLECTIONREQUEST']._serialized_start=737
  _globals['_CREATECOLLECTIONREQUEST']._serialized_end=932
  _globals['_CREATECOLLECTIONRESPONSE']._serialized_start=934
  _globals['_CREATECOLLECTIONRESPONSE']._serialized_end=1049
  _globals['_DELETECOLLECTIONREQUEST']._serialized_start=1051
  _globals['_DELETECOLLECTIONREQUEST']._serialized_end=1088
  _globals['_GETCOLLECTIONSREQUEST']._serialized_start=1090
  _globals['_GETCOLLECTIONSREQUEST']._serialized_end=1195
  _globals['_GETCOLLECTIONSRESPONSE']._serialized_start=1197
  _globals['_GETCOLLECTIONSRESPONSE']._serialized_end=1294
  _globals['_UPDATECOLLECTIONREQUEST']._serialized_start=1297
  _globals['_UPDATECOLLECTIONREQUEST']._serialized_end=1519
  _globals['_SYSDB']._serialized_start=1522
  _globals['_SYSDB']._serialized_end=2216
# @@protoc_insertion_point(module_scope)
